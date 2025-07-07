### Remote에서 삭제된 브랜치 로컬에서도 삭제하기
~~~bash
git branch -vv \
  | grep ': gone]' \
  | awk '{print $1}' \
  | xargs -r git branch -d
  ~~~ 
