## The Linux Filesystem

The Linux Filesystem can be a little tricky for Windows users to get their head around initially.

**In Linux, everything is a file**:

- **Regular files**: documents, images, code
- **Directories**: folders that contain other files
- **Devices**: hard drives, keyboards, USB ports
- **Processes**: running programs

It's those last two that confuse people, thinking of a keyboard as a file. The idea is that it is represented by a file, and we can work with everything in the same way that we work with files.

**Linux uses a single-root filesystem** - In Windows you are likely familiar with each storage device on your system having a drive letter assignment, typically the disk on which Windows is installed is assigned `c:`, subsequent ones are `d:`, `e:`, and so on. Each of these storage disks then has it's own filesystem of directories and files which you can navigate around, and move from one drive to another.

Linux is different, it has a filesystem which unifies everything under one structure, including multiple storage devices if attached. The very top of the structure is called `root`, and is represented by `/`.

**Key Directories**: Below you can see some examples of the key directories in the `Filesystem Hierarchy Standard` that sit below root, including what they contain. Don't worry about memorising them, they're just provided for context.

```Bash
 / # root
 |
 |--bin # Essential user command binaries
 |--boot # Boot loader files
 |--dev # Device files
 |--etc # System configuration files
 |--home # User personal directories
 |    |-centos # centos user's home directory
 |--lib # Shared libraries and kernel modules
 |--media # Removable media mount points
 |--mnt # Temporary mount points
 |--root # Root user's home directory
 |--sys # Kernel and device information
 |--tmp # Temporary files
 |--var # Variable data that changes
```

### Explore the Filesystem - Mini-Lab

1. Move to the root of the filesystem with `cd /`
2. Type `ls` to list the contents of root
3. Use a combination of `cd` and `ls` to explore the filesystem, including some of the directories listed above.

>`Root` can refer to both the top of the filesystem, but the most powerful use on the system is also called the `root` user. Ensure that you understand which root is being referred to when discussing work!

### Absolute and Relative Paths

The location to any particular file in a Linux filesystem can be referenced in two ways, using either the `absolute` or the `relative` path.

#### Absolute Paths

The top of the filesystem is root, we can then use cd to move into a sub-directory, and another sub-directory, and so on. However many directories we dive into, we can provide a path to our location starting from root, or to a specific file object in that location.

```Bash
# Absolute path to the centos user's home directory
/home/centos
# Absolute path to a file in a project folder, in the centos user's home directory
/home/centos/my_project/my_file
```

The absolute path is useful when you need to ensure a particular file, such as a configuration file, is always referenced at the correct location. Automation scripts are also typically given absolute paths, so that it operates correctly regardless of where it is called from.

#### Relative Paths

Relative paths are provided from the current location in the filesystem, so if you're currently in the centOS user's home location, then the relative path to a file in your projects folder would be

```Bash
# Relative path
my_project/my_file

# Absolute path
/home/centos/my_project/my_file


# |-------absolute-path---------|
#             |--relative-path--|
# /home/centos/my_project/my_file
```

The relative path is particularly useful when working on projects in which everything is contained within a working directory, use relative paths in your code to locate resources within the directory. Then, when you want to share your project, you can copy the whole working directory; regardless of where the receiver decides to save it on their computer, the relative paths will still function.

There are two useful shortcuts when using relative paths:

- `.` - (a single period) always references the current directory
- `..` - (double period) always references the parent directory

## Working With Files

Remember, everything is a file, and you will spend a lot of your time in Linux working with files.

>Linux doesn't really recognise file extensions the way Windows does. You will see file extensions, but generally they're used to help the human users find what they need, for example configuration files usually end with something like `.conf` or `.cfg`

### Finding Files

The `find` command allows you to search for a file in a given location

```Bash
find ./ -name "my_file"
```

- `find`: Command
- `./`: The current location (argument)
- `-name`: The **name** option lets me specify the name of the file to search for

>In addition to `-name`, other options allow you to find files by size, age, permissions, type, and many more

#### Finding Programs

Use the `whereis` command to locate the files and resources related to a program.

```Bash
whereis nano
```

### Wildcards

Wildcards allow you to replace characters in a file path, which can be used to identify groups of related files, or find files where the whole name is unknown. There are two wildcards we can use.

- `?`: Placeholder for a single character
- `*`: Placeholder for any number of characters

#### Wildcards Mini-Lab

1. In your home directory, create a directory called `test`
2. Move into your `test` directory and create 4 files: `file1`, `file2`, `my_file`, & `your_file`.
3. Return to the parent directory.
4. Use the `ls` command and wildcards to list the relevant files in the `test` directory.

```Bash
ls /test # List all files in test directory
ls /test file? # Returns file1 and file2
ls /test *file # Returns my_file and your_file
```

### GREP (`G`lobal `R`egular `E`xpressions `P`rint)

Grep is an implementation of regular expressions (RegEx) which a utility which allows you to define string patterns, which can be used to search through an input for matches to the defined pattern.

Grep is a powerful tool with countless ways to utilise it, such as:

- Searching log files for `errors`, `failures`, `permission denied` responses, or whatever you want.
- Searching unstructured text files for data that matches the pattern of an email address, dates, phone numbers, and so on.

Grep includes lots of special characters to create various different complex string patterns to search for, but for our purposes we can keep it simple, and just use it for text matching.

#### Grep Mini-Lab

1. Move to your home location
2. Create a text file and open it with Nano (or vi/vim)
3. Visit this [wikipedia page](https://en.wikipedia.org/wiki/Pale_Blue_Dot), copy the reflections quote, and paste it into your text file (Use `CTRL+J` on each line to justify).
4. Save your file (I've called it `pale_blue_dot`) and close the editor.
5. Use grep to perform searches within the file with `[grep] [search_term]  [filename]`

```Bash
grep earth pale_blue_dot # No results returned

grep Earth pale_blue_dot # Results returned - grep is case sensitive

grep [Ee]arth pale_blue_dot # Results returned - a simple regex expression to match examples with either `E` or `e`
```

Now repeat the task with another block of text, try to do it without referring back to the instructions.

>Notice, we didn't use any file extension to let linux know this was a text file.