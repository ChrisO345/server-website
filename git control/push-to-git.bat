@echo off
git add .
set /p message="Enter Commit Message: "
git commit -m message
git push origin master
@echo on