import re 
import sys
import argparse



def vcdconcatduplicate(input_file_list,n,output_file):
    timescale=""
    initial_time=-1
    end_time=0
    with open(output_file,"w") as vcdOutput:
        ## get the first file 
        foundEnd=False
        with open(input_file_list[0],"r") as fin:
            line=fin.readline()
            while line:
                if "$enddefinitions" in line:
                    foundEnd=True
                if foundEnd and line.startswith("#"):
                    if initial_time==-1:
                        initial_time=int(line.lstrip("#"))
                    else:
                        end_time=int(line.lstrip("#"))
                vcdOutput.write(line)
                line=fin.readline()
        print("Timescale: " + str(timescale))
        print("Initial time: "+ str(initial_time))
        print("End time : " +str(end_time)) # this is gonna be the start time for the next files 
        for i in range(1, n):
            time_offset = end_time * i
            with open(input_file_list[0], "r") as fin:
                foundEnd = False
                line = fin.readline()
                while line:
                    # Start duplicating only after $enddefinitions
                    if "$enddefinitions" in line:
                        foundEnd = True
                    # Adjust timestamps after $enddefinitions
                    if foundEnd and line.startswith("#"):
                        # Increment the timestamp by the time offset
                        current_time = int(line.lstrip("#"))
                        new_time = current_time + time_offset
                        vcdOutput.write(f"#{new_time}\n")
                    else:
                        # Write the line without changes for non-timestamp lines
                        vcdOutput.write(line)
                    line = fin.readline()
    print("Final End time : " +str(new_time))

def vcdconcat(input_file_list,output_file):
    timescale=""
    initial_time=-1
    end_time=0
    with open(output_file,"w") as vcdOutput:
        ## get the first file 
        foundEnd=False
        with open(input_file_list[0],"r") as fin:
            line=fin.readline()
            while line:
                if "$enddefinitions" in line:
                    foundEnd=True
                if foundEnd and line.startswith("#"):
                    if initial_time==-1:
                        initial_time=int(line.lstrip("#"))
                    else:
                        end_time=int(line.lstrip("#"))
                vcdOutput.write(line)
                line=fin.readline()
        print("Timescale: " + str(timescale))
        print("Initial time: "+ str(initial_time))
        print("End time : " +str(end_time)) # this is gonna be the start time for the next files 
        for input_file in input_file_list[1:]:
            foundEnd=False
            with open(input_file, "r") as fin:
                line=fin.readline()
                while line:
                    if "$enddefinitions" in line:
                        foundEnd=True
                    if foundEnd:
                        if line.startswith("#"):
                            new_time=end_time+int(line.lstrip("#"))
                            line="#"+str(new_time)+"\n"
                        vcdOutput.write(line)
                    line=fin.readline()
        print("Final End time : " +str(new_time))


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-files", type=str, nargs="+", 
                        help="input vcd/evcd file to merge")
    parser.add_argument("--iterations", type=int,
                        help="number of iterations of single input file to dump")
    parser.add_argument("--output-file", type=str,
                        help="output vcd file")
    args = parser.parse_args()
    if args.iterations > 0 and len(args.input_files) >1 :
        print("Error cannot add multiple vcd files and duplicate their execution")
        sys.exit(-1)
    if args.iterations > 0 and len(args.input_files)==1:
        vcdconcatduplicate(args.input_files,args.iterations,args.output_file)
    else:
        vcdconcat(args.input_files,args.output_file)
    sys.exit()