doTermux() {
	rm -rf $PREFIX/bin/faang
	rm -rf $PREFIX/share/faang
}
doGnuLinux() {
	sudo rm -rf /usr/local/bin/faang
	sudo rm -rf /usr/share/faang
}

doUninstall() {
	echo -n "[*] Uninstalling faang..."
	if [ "$(uname -o)" = "Android" ]; then
		doTermux
	else
		doGnuLinux
	fi
	echo -e "[DONE]"
}
doUninstall