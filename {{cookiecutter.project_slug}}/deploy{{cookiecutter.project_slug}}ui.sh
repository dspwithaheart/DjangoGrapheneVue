echo 'Build {{cookiecutter.project_slug}}ui'
# If SSL error occurs, run the following command
# pip3 install --upgrade certifi
export SSL_CERT_FILE=$(python -m certifi)

nodeVersion='22.11.0'
if [ $(node --version | grep -c $nodeVersion) -eq 0 ]; then
  echo "Creating nodeenv..."
  nodeenv --node=$nodeVersion -p

  npm ls
fi

# For first run, check if project exists
cd ./src/
if [ ! -d "./{{cookiecutter.project_slug}}ui/src" ]; then
  echo "Initialize UI...."

  npm create vue@latest {{cookiecutter.project_slug}}ui

  cd {{cookiecutter.project_slug}}ui
  cp ../vite.config.ts.default vite.config.ts
  echo Init install, format and type-check.
  npm install
  npm run format
  npm run type-check

  cd ..
  echo Done init.
fi
# Go back to project root
cd ..

npm install ./src/{{cookiecutter.project_slug}}ui
npm run --prefix ./src/{{cookiecutter.project_slug}}ui build
echo '{{cookiecutter.project_slug}}ui build complete!'
