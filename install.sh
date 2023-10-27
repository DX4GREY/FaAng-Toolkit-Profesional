#!/bin/bash
pathName="faang"
mainFile="main.py"
optDir="opt"

doTermux() {
	mkdir -p $PREFIX/$optDir
	rm -rf $PREFIX/bin/$pathName
	mkdir -p $PREFIX/$optDir/$pathName
	cp -r -f modules/* $PREFIX/$optDir/$pathName
	chmod +x $PREFIX/$optDir/$pathName/$mainFile
	ln -s $PREFIX/$optDir/$pathName/$mainFile $PREFIX/bin/$pathName
}
doGnuLinux() {
	sudo mkdir -p /usr/$optDir
	sudo rm -rf /usr/local/bin/$pathName
	sudo mkdir -p /usr/$optDir/$pathName
	sudo cp -r -f modules/* /usr/$optDir/$pathName
	sudo chmod +x /usr/$optDir/$pathName/*
	sudo ln -s /usr/$optDir/$pathName/$mainFile /usr/local/bin/$pathName
}
installRequirements() {
	echo -n "[*] Checking python if installed..."
	if [ -x "$(command -v python)" ]; then
		echo -e "[INSTALLED]"
	else
		echo -e "[NOT INSTALLED]"
		echo -e "Installation aborted..."
		echo -e "Please install python then try again..."
		exit
	fi
	
	echo -e "[*] Installing dependencies..."
	pip install -r requirements.txt
	echo -e "[*] Done. just run : $pathName"
}

doInstall() {
	echo -n "[*] Installing $pathName..."
	if [ "$(uname -o)" = "Android" ]; then
		doTermux
	else
		doGnuLinux
	fi
	echo -e "[DONE]"
	installRequirements
}
doInstall