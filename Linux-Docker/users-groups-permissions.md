# Users, Groups, and Permissions

## Linux User Accounts

User accounts in a Linux system are stored in a file called `passwd` located in the `/etc` directory, view it with `sudo cat /etc/passwd`.

Here is a section of the output, each line represents a different user.

```Bash
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin

...

sshd:x:74:74:Privilege-separated SSH:/usr/share/empty.sshd:/sbin/nologin
systemd-oom:x:992:992:systemd Userspace OOM Killer:/:/usr/sbin/nologin
centos:x:1000:1000::/home/centos:/bin/bash
```

We'll break down one entry in the file, but we're not aiming to become Linux administrators, so don't worry about memorising it.

```Bash
centos:x:1000:1000:[comment]:/home/centos:/bin/bash
```

- `centos`: Username.
- `x`: Placeholder for the password, which is located in a different file (`shadow`)
- `1000:1000`: (UserID:GroupID) Every user account has a unique user ID number, which simply increments for each new user, the next one will be 1001; Each user also has an associated group, which also has a unique ID number. *These numbers start the same, but do not have to match*.
- `[comment]`: Not used in the example on your VM, but it can be used to enter optional information. Examples include the user's full name, or deparment.
- `/home/centos`: The path to the user's home directory. 
- `/bin/bash` Path to the user's default shell

>Notice only two entries reference the Bash Shell, `root` and `centos`. The other accounts that end in `/sbin/nologin` are system accounts used by services, and not intended for human users to access.

## Linux Groups

`Groups` on a computer system are a common feature for making administration easier. They allow us to assign permissions or carry out admin and management tasks once, and have them apply to all of the members in a group. View the groups with: `cat /etc/group`

A group is created for each new user, therefore every Linux user account is in at least one group which they’re in control of. The user can add other users to their group to share their files if they wish. Users can also be added to additional groups, providing access to other resources.

You can create supplemental groups (using the `groupadd` command), such as for business departments, functions, or projects, then add the relevant users to that group (using the `usermod` command). You can then assign permissions to the group, permitting access to the department or project's data and resources to all members.

## Linux Permissions

**Everything in Linux is a file** (more on that later), every file has an `owner`, and is within a `group`. Typically the owner is the person who created the file, and the file will be in their group by default. (*Although we can change this behaviour if we need to*).

To view some permissions, if you still have a directory containing some test files move into it, or create them if needed. Type `ls -l` and you should see an output like this:

```Bash
-rw-r--r--. 1 centos centos    0 Apr 12 00:35 file1
-rw-r--r--. 1 centos centos    0 Apr 12 00:35 file2
-rw-r--r--. 1 centos centos    0 Apr 12 00:32 my_file
-rwxrwxrwx. 1 centos centos 2288 Apr 12 13:58 pale_blue_dot
-rw-r--r--. 1 centos centos    0 Apr 12 00:35 your_file
```

Here's a breakdown of one line: `-rwxrwxrwx. 1 centos centos 2288 Apr 12 13:58 pale_blue_dot`

- `-rwxrwxrwx`: Permission string NOTE: I've changed mine from the default for illustration purposes.
  - `-`: The first dash represents the type of file, in this case it's a `standard` file, but you will see `d` for `directory`, and others values that our beyond our scope.
  - `rwx`: These values represent the permissions that we can assign to our files.
    - `r`: read the file
    - `w`: write to the file (edit/save)
    - `c`: execute the file (run it as an app/script)
  - `rwxrwxrwx`: The permission set occurs three times, representing three different entities:
    - The first block of three permissions represents the `owner` of the file
    - The second block represents the users who are in the same `group` as the file
    - The third block represents `other` users, who are not the owner, or in the same group.
- `1`: Number of hard-links (out of scope for our purposes)
- `centos centos`: The file's `owner`, and the `group` it is in.
- `2288`: The size of the file
- `Apr 12 13:58`: Last modified timestamp (`touch` updates this)
- `pale_blue_dot`: File name

### Users and Groups Lab

Practice working with user accounts and groups by completing this lab:

[Users and Groups Lab](./users-groups-lab.md)

### Modifying Permissions

We can modify the permissions of a file in Linux in two different ways: `Absolute`, and `Symbolic` modes, but both options use the command: `chmod`.

#### Absolute Mode

Absolute mode uses `Octal` numbers to represent the three user entities (`owner`/`group`/`others`), which can be calculated using three bits of binary.

>This is a bit out of scope, feel free to skip to `symbolic` mode, but if you're interested...

- Three binary bits _ _ _ align with the three permissions r w x; If the bit is `ON` (1), the entity has that permission, if it's `OFF` (0) they do not have that permission.
- The three bits are in the 4, 2, 1 positions, so if the read bit is on, then it has a value of 4.
- Any combination of those three bits will give us a different value, all three permissions would be `4 + 2 + 1 = 7`

|Permissions|Values|Sum|
|---|---|---|
|r w x|4+2+1|7|
|r w -|4+2+0|6|
|r - x|4+0+1|5|
|r - -|4+0+0|4|
|- w x|0+2+1|3|
|- w -|0+2+0|2|
|- - x|0+0+1|1|
|- - -|0+0+0|0|

The above table allows us to represent any combination of Read, Write, and Execute, with a single number between 0-7.

>`Octal`, also known as Base-8, is a number system which uses only the values 0-7 (8 different digits), which can be represented with three bits of binary, as seen. `Binary` uses 0-1 and is also known as Base-2; Decimal uses 0-9, also known as Base-10; Hexadecimal uses 0-F, also known as Base-16. Why do you think Octal and Hex are prevalent in computing?

The above table refers to a single group of three, for example just the permissions for the owner of the file, but the group and other permissions work just the same; You can define all of the permissions for all users with three numbers, such as 544 (r-xr--r--).

```bash
sudo chmod 777 file1 # Assign rwx permissions for all user types.
```

- `chmod`: The change mode command (referring to file mode bits)
- `777`: The Absolute permissions - DO NOT USE `777`, this gives everyone full access.
- `file1`: The filename provided as an argument.

#### Symbolic Mode

Symbolic mode is arguably the easier way to manage permissions, although you may need several commands to achieve the same thing as one in absolute mode.

With symbolic mode we use three components to modify permissions, the class (the owner/group/other), the operator to specify the type of change (add, remove, or reset), and finally the mode which is the specific permission to modify (read/write/executy). The symbols are as follows.

|Class||
|---|---|
|`u`|user (owner)|
|`g`|group|
|`o`|others|
|**Operator**||
|`+`|Add a permission|
|`-`|Remove a permission|
|`=`|set to exactly...|
|**Mode**||
|`r`|Read|
|`w`|Write|
|`x`|Execute|

Example usage

```bash
chmod u+x file1 # Add the execute permission (mode) to file1 for the owner

chmod g-w file2 # Remove the execute permission from file2 for the users in the same group as the file

chmod o=rw my_file # Set the permissions for other users to read and write against my_file
```

### Modifying Owner and Groups

Every file has an owner user and a group, you can modify this with the `chown` command: `chown [new_user]:[new_group] [filename]`

```Bash
sudo chown root:root file1 # Change owner and group to root
ls -l # Confirm owner/group change
sudo chown centos:centos file1 # Change owner and group back to centos
ls -l # Confirm owner/group change
```

## Sudo

You will have come across many examples of commands which are preceded with the word sudo (`S`uper `U`ser `Do`). This allows us to run a command with root user privileges, without having to switch to the root user account.

As we've mentioned previously, the `root` user account is the most powerful account on a Linux system, which has permission to do anything, and access anything.

>It is **highly** recommended that the root user account is not used on a daily basis, and access to the credentials is restricted.

Most users will log onto the system with a standard user account which, when freshly created, only have permission to create and edit files in their home directory. However, there are common administration tasks, which are done regularly, but do require elevated privileges. For example user management, installing and managing packages (apps), changing system configuration, etc.

>You should always follow the `Principal of Least Privilege` which satates that you should only grant the minimum permissions required for a user to carry out their role.

To enable a standard account to perform elevated actions we add them to the sudoers file. You can grant privileges to individual users, or to whole groups for all commands or individual ones, sometimes with or without a password.

Once permission has been granted through the sudoers file, the user in question can initiate a command using elevated permissions by prefixing it with sudo.

>RHEL based Linux distributions, like CentOS, also have a wheel group, managed through the sudoers file. Adding a user to this group provides full sudo access - this is how the centos account has been configured for the purpose of learning - but this is NOT recommended in live environments.
