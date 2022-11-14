""" Create a function that converts any string value to a
Sentence  case,  Then  write  a  unit  test  that  checks  the
function's correctness.
"""


""" def sen_case():
    sentence = "Python lessons for testers."
    convert_sentence = sentence.title()
    print(convert_sentence)


sen_case()"""


def to_sentence_case(val):
    result = val[0].upper() + val[1:]
    print(result)


to_sentence_case("Great is your faithfulness")
