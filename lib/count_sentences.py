#!/usr/bin/env python3
import re

class MyString:
  __value = ""
  def __init__(self,value=""):
      self.__value = value

  def set_value(self,value):
    if(type(value) is not str):
      print("The value must be a string.")
    else:
      self.__value = value

  def get_value(self):
    return self.__value

  def is_sentence(self):
    if(self.__value[-1] == "."):
      return True
    else:
      return False
  def is_question(self):
    if(self.__value[-1] == "?"):
      return True
    else:
      return False
  def is_exclamation(self):
    if(self.__value[-1] == "!"):
      return True
    else:
      return False
  def count_sentences(self):
    sentences = re.split('[.!?]',self.__value)
    for i in range(sentences.count("")):
      sentences.remove("")
    print(sentences)
    return len(sentences)
  value = property(get_value,set_value,)

