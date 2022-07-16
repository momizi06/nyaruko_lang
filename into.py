#!/usr/bin/python3

"""うーにゃーとか言ってるのをちかんする"""
import os

text = ""
with open("haiyoru_konton.nyaruko", mode="r") as file:
    text = file.read()
    text = text.replace("(」・ω・)」うー(／・ω・)／にゃー", "ウエエエエエエエエエエエアアアアアア！！！")
    text = text.replace("(」・ω・)」うー!(／・ω・)／にゃー!", "( 'ω')/<ウオオオオオアアアーーーッ！！！")
    text = text.replace("(」・ω・)」うー!!(／・ω・)／にゃー!!", "！！！アアアアアアエエエエエエエエエエエウ")
    text = text.replace("(」・ω・)」うー!!!(／・ω・)／にゃー!!!", "( 'ω')/<ウオオオオオアエアーアート！！！")
    text = text.replace("CHAOS☆CHAOS!", "いや草に草を生やしてさらに草を飾って草アートを描きたいレベルで草")
    text = text.replace("I WANNA CHAOS!", "菅さんに菅さんを生やしてさらに菅さんを飾って菅さんアートを描きたいレベルで菅さん")
    text = text.replace("Let's＼(・ω・)／にゃー", "ああそうだねえええええええええええええ！！！")
    text = text.replace("cosmic!", "ウニャアアアアアアアアアアアアアアア！！！")
    print(text)

with open("chaos.muhothi", mode="w") as file:
    file.write(text)
