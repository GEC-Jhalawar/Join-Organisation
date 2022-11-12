import json
import pathlib
import re
from datetime import date
root = pathlib.Path(__file__).parent.parent.resolve()


def replace_writing(content, chunk):
    r = re.compile(
        r'<!\-\- Student Data Start \-\->.*<!\-\- Student Data End \-\->',
        re.DOTALL,
    )
    chunk = '{}'.format(chunk)
    return r.sub(chunk, content)


if __name__ == '__main__':
    readme_path = root / 'README.md'
    list_path = root / 'utils/StudentList.json'
    readme = readme_path.open().read()
    list = list_path.open().read()
    StudentList = json.loads(list)
    tables = ''
    for key in StudentList:
        data = ''
        for student in StudentList[key]:
            data += '  <tr>\n    <td>'+ student.get("Name") + '</td>\n    <td>'+ student.get("Roll") + '</td>\n    <td>'+ student.get("Email") + '</td>\n    <td><a href="https://github.com/' + student.get("Github username") + '">'+ student.get("Github username") + '</a></td>\n  </tr>'
        tables += '### '+key+'\n\n<table align="center">\n  <thead>\n    <tr>\n      <td>Name</td>\n      <td>Roll</td>\n      <td>Email</td>\n      <td>Github username</td>\n    </tr>\n  </thead>\n  <tbody>\n' + data + '\n  </tbody>\n</table>\n\n\n'
    content = '<!-- Student Data Start -->\n' + tables + '<!-- Student Data End -->'
    rewritten_entries = replace_writing(readme, content)
    readme_path.open('w').write(rewritten_entries)