#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value=""):
    if(type(value) == str):
      print("The value must be a string.")
    else:
      self.value = value

  # def set_value(self,value):
  #   if(type(value) is not str):
  #     print("The value must be a string.")
  #     self._value = "The value must be a string."


  #   else:
  #     self.value = value
  # def get_value(self):
  #   return self.value

  def is_sentence(self):
    if(self.value[-1] == "."):
      return True
    else:
      return False
  def is_question(self):
    if(self.value[-1] == "?"):
      return True
    else:
      return False
  def is_exclamation(self):
    if(self.value[-1] == "!"):
      return True
    else:
      return False
  def count_sentences(self):
    sentences = re.split('[.!?]',self.value)
    for i in range(sentences.count("")):
      sentences.remove("")
    print(sentences)
    return len(sentences)


string = MyString(3000)
string.value = 3000