STRINGIFIED_DICT_1 = '''{
 hello: world
 is: true
 nested: {
  count: 5
 }
}'''

STRINGIFIED_DICT_2 = '''{
    hello: world
    is: true
    nested: {
        count: 5
    }
}'''

STRINGIFIED_DICT_3 = '''{
|-|-hello: world
|-|-is: true
|-|-nested: {
|-|-|-|-count: 5
|-|-}
}'''

STRINGIFIED_DICT_INDENTED_1 = '''{
        hello: world
        is: true
        nested: {
            count: 5
        }
    }'''

STRINGIFIED_DICT_INDENTED_2 = '''{
      hello: world
      is: true
      nested: {
          count: 5
      }
  }'''

STRINGIFIED_DICT_INDENTED_3 = '''{
            hello: world
            is: true
            nested: {
                count: 5
            }
        }'''

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

NESTED_DIFF_STR_12 = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''  # noqa: W291
