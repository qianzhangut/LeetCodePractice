git add "$(git status -s | sed "s@^[^ ]* @$PWD/@")"
git commit -m "$(git status -s | sed "s@^[^ ]* @$LS/@")"
git push origin master
