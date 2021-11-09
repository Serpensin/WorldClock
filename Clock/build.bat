set /p id="Enter Version: "
nuitka "Clock.py" --standalone --onefile --windows-company-name="Serpent Modding" --windows-product-name="WorldClock" --windows-file-version=%id% --windows-file-description="Simple WorldClock" --enable-plugin=anti-bloat --windows-onefile-tempdir --windows-icon-from-ico=C:\Users\wissm\OneDrive\Bilder\ICO\clock.ico
