echo off

del !ARCHIVES\*.*

rd !ARCHIVES\

for /d %%X in (*) do "c:\Program Files\7-Zip\7z.exe" a "%%X.zip" "%%X\" 

mkdir "!ARCHIVES\"

move *.zip !ARCHIVES\

pause