# Gitlab 使用笔记

- rules 使用正则表达式
  - [目前正则表达式只能是字面字符串，不能使用变量][3]

  ```yml
  rules:
    - if: '$VARIABLE =~ /^content.*/'
  ```

- [删除 Release][2]
  - Go to Project Overview -> Releases
  - Click the release you want to delete
  - Scroll to the bottom. Find the tag icon. Click on the tag.
  - There is a trash can button for the tag. Deleting the tag will delete the release as well.

- [job script 使用特殊字符时（比如冒号）需要用引号括起来。][1]

  [1]: https://docs.gitlab.com/ee/ci/yaml/script.html#use-special-characters-with-script
  [2]: https://stackoverflow.com/a/63810511
  [3]: https://gitlab.com/gitlab-org/gitlab/-/issues/209904
