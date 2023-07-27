# prod-catalog

1. first installl git lfs: steps(for mac, run these cmds in terminal )
   1.  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   2.   (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/prathiksha.sb/.zprofile
   3.   eval "$(/opt/homebrew/bin/brew shellenv)"
   4.    brew install git-lfs
   5. git lfs install
2. after installing brew and git lfs, move to repo folder and open terminal
3. run these cmds:
   1. brew update
   2.  git lfs track "*.json"
   3.   git lfs push --all origin main
   4.   git add .
   5.   git commit -am "add large file"
   6.   git push -u origin main  <if this gives error, run the 7. cmd>
   7.   git lfs migrate import --include="*.json"  <again run 6.>
4. now large file (which in current case was a json file) will be pushed to repo
