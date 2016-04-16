#HexPy

HexPy is a project focused on using arrays of 8-byte color hexcodes. 
**The old readme is now outdated**

####To see the latest stable release of HexPy, [click here](https://github.com/Tacolizard/HexPy/releases/latest)

The main part of HexPy, `pgexec`, is a program to output an array (or 'list') of hexcodes. It has a simple gui menu, and is accessed from  a CLI, though an importable library is planned. `pgexec` is designed to be able to use almost any hex array you throw at it, and to not care about format. You can even feed it arrays generated by non-Python programs. The only requirement is a variable, `w`, to specify image width. For an example of the format, [click here](https://github.com/Tacolizard/HexPy/blob/master/pgexec/imgtest.pgf)

`pgexec` guide:

###Installation is easy:
1. Have Python 3.4 or later installed. 
**<strike>Note: on most Linux distros, you must install `python3-tk` as well</strike>**
**v2.0-release: `pgexec` now automatically downloads dependencies**
2. Download and decompress the `.zip` or `.tar` from Github
3. `cd` to the uncompressed directory
4. Do `chmod 777 pgexec`
5. Either add it to your PATH or run it with `./pgexec`

###To test HexPy:
1. Use a pre-made image or run the `ranhex.py` script to generate a test image.
2. From a terminal do `pgexec myimage.pgf`
You can also add a `v` at the end if you want to see live stats and errors raised directly from Python.
However, `v` tends to impact performance pretty heavily.
