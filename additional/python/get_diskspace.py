import jessentials

def main():
    lines = jessentials.run_command("df -h", False, True) 
    already_printed_drives = []
    for line in lines:
        if line.startswith("df:"):
            continue
        if line.startswith("udev"):
            continue
        if line.startswith("tmpfs"):
            continue
        if line.startswith("/dev/loop"):
            continue
        if line.startswith("revokefs-fuse"):
            continue
        if line.startswith("cgroup"):
            continue
        if line.startswith("Filesystem"):
            continue
        line : str = line
        values = line.split(" ")
        while("" in values):
            values.remove("")

        # Ignore disks which are smaller than 1G.
        if values[1].endswith("M"):
            continue
        
        # For btrfs: Hide volumes
        if (not values[0] in already_printed_drives):
            print("%s\t%s\t%s\t%s\t%s\t%s" % (values[0], values[1], values[2], values[3], values[4], values[5], ))
            already_printed_drives.append(values[0])
        

        


if __name__ == '__main__':
    main()