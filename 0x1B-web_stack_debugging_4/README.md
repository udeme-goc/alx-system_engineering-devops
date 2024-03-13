# Web Stack Debugging #4

This project aims to debug a web server setup featuring Nginx to handle high concurrency and resolve issues related to failed requests.

## Description
In this project, we encountered a scenario where a web server setup featuring Nginx was experiencing a large number of failed requests under high load. The goal was to diagnose the issue and implement fixes to ensure the server could handle the load effectively.

## Puppet Manifests
- `0-the_sky_is_the_limit_not.pp`: Fixes the issue of failed requests by adjusting Nginx configuration to handle high concurrency.
- `1-user_limit.pp`: Increases the file descriptor limit for the holberton user to resolve "Too many open files" errors.

## Usage
To apply the Puppet manifests, use the `puppet apply` command followed by the filename. For example:

```bash
$ puppet apply 0-the_sky_is_the_limit_not.pp
$ puppet apply 1-user_limit.pp
```

## Dependencies
-  Puppet

## Author
Created by Udeme Harrison as part of the curriculum of the ALX SE Programme.
