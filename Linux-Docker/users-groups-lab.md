# Users and Groups Lab

This lab will guide you through the following tasks:

- Create a file owned by one user.
- Verify another user cannot access it.
- Create a group, add both users, assign the file to the group.
- Verify both can now read it.

1. Create a test directory

```bash
sudo mkdir users-groups
cd /users-groups
```

2. Create a test file as your current user

```bash
echo "Confidential data" > secret.txt # echo [string]; redirect output to file
ls -l # Verify file owner and group are centos
```

3. Make sure only owner can read

```bash
chmod 600 secret.txt
```

4. Create user 'alice'

```bash
sudo useradd -m -s /bin/bash alice # View `useradd --help` to review options
sudo passwd alice   # Set a password (e.g., 'alice123')
```

5. Create user 'bob'

```bash
sudo useradd -m -s /bin/bash bob
sudo passwd bob     # Set a password (e.g., 'bob123')
```

6. Switch to alice

```bash
su - alice # su = switch user
```

7. Try to read the file

```bash
cat /lab/users-groups/secret.txt # Expected: Permission denied
```

8. Try to list directory (if directory permissions allow)


```bash
ls -l /lab/users-groups/secret.txt # Expected: Permission denied
exit   # Back to original user
```

9. Create a shared group

```bash
sudo groupadd project_team
```

10. Add both users to the group

```bash
sudo usermod -aG project_team alice # a = append; G = Groups
sudo usermod -aG project_team bob
```

11. Verify group membership

```bash
groups alice
groups bob
```

12. Change group ownership of the file

```bash
sudo chown :project_team /lab/users-groups/secret.txt
```

13. Set permissions: owner rw; group rw; others none

```bash
sudo chmod 660 /lab/users-groups/secret.txt
```

14. Verify permissions

```bash
ls -l /lab/users-groups/secret.txt
# Output should look like: -rw-rw---- 1 root project_team ...
```

15. Verify both users can access:
- As Alice:

```bash
su - alice
cat /lab/users-groups/secret.txt
# Should show: Confidential data
exit
```

- As Bob:

```bash
su - bob
cat /lab/users-groups/secret.txt
# Should show: Confidential data
exit
```

16. Cleanup

```bash
sudo userdel -r alice
sudo userdel -r bob
sudo groupdel project_team
sudo rm -rf /lab/users-groups
```

## Command Summary

|Command|Purpose|
|---|---|
|`useradd`|Create user (Adds user to /etc/passwd)|
|`groupadd`|Create group (Adds group to /etc/group)|
|`chown :group`|Change group (Assigns group ownership)|
|`chmod 660`|Permissions (Owner+group = rw, others = none)|
|`su - user`|Switch user|
