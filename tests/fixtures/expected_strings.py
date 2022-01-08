PLAIN_DIFF_STR_12 = '''{
    float: 1.0
  - follow: false
    host: hexlet.io
    married: null
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

PLAIN_DIFF_STR_21 = '''{
    float: 1.0
  + follow: false
    host: hexlet.io
    married: null
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: true
}'''
