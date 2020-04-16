{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week4-A107260093-林芷妤.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN+WmQjd60/J/aazMnwu0fK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/CHIH-YU-LIN/introduction-to-data-science/blob/master/week4_A107260093_%E6%9E%97%E8%8A%B7%E5%A6%A4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kcMD5s7Z8oTL",
        "colab_type": "code",
        "outputId": "99c7fb45-e42d-41aa-e272-a493b137759c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "current_celsius = 16\n",
        "current_fahrenheit = current_celsius * 9 / 5 + 32\n",
        "print(current_fahrenheit)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "60.8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7G2mvGmc81rr",
        "colab_type": "code",
        "outputId": "0e050949-f89d-4bce-eaf8-f281e9993658",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "shaq_height = 216\n",
        "shaq_weight = 147\n",
        "shaq_bmi=shaq_weight/(shaq_height/100)**2\n",
        "print(shaq_bmi)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "31.507201646090532\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nFX6j7Kg_YJ-",
        "colab_type": "code",
        "outputId": "d3b360ef-3b34-43b1-d78f-f49c0df85e66",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "ross_said=\"Let's put aside the fact that you \\\"accidentally\\\" pick up my grandmother's ring.\"\n",
        "print(ross_said)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "doqwStYEAU0D",
        "colab_type": "code",
        "outputId": "5e1c20f6-9dae-47d9-9c42-39b2f8d452aa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "ross_said='Let\\'s put aside the fact that you \"accidentally\" pick up my grandmother\\'s ring.'\n",
        "print(ross_said)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "O2IS79FoAk67",
        "colab_type": "code",
        "outputId": "4f8ed17f-117d-4644-a116-bd51c530f0d8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "ross_said = \"\"\"Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\"\"\"\n",
        "print(ross_said)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FUnbbzBNAm1u",
        "colab_type": "code",
        "outputId": "e72ddd4d-acb1-4674-e900-0372cb43cee2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 69
        }
      },
      "source": [
        "city = input(\"請輸入城市名:\")\n",
        "weather = input(\"請輸入天氣:\")\n",
        "print(\"我在{}，天氣{}\".format(city,weather))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入城市名:台北\n",
            "請輸入天氣:陰\n",
            "我在台北，天氣陰\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3fOM7WMXCP5W",
        "colab_type": "code",
        "outputId": "2fffb2c5-3b47-4f87-f011-c30474b7c7ed",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 104
        }
      },
      "source": [
        "name = input(\"請輸入球員姓名:\")\n",
        "shaq_height = eval(input(\"請輸入球身高:\"))\n",
        "shaq_weight = eval(input(\"請輸入球體重:\"))\n",
        "shaq_bmi = shaq_weight/(shaq_height/100)**2\n",
        "print(\"{}的身體質量指數為：{:.2f}\".format(name,shaq_bmi))\n",
        "print(\"{}是否過重：{}\".format(name,shaq_bmi>30))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入球員姓名:俠客歐尼爾\n",
            "請輸入球身高:216\n",
            "請輸入球體重:147\n",
            "俠客歐尼爾的身體質量指數為：31.51\n",
            "俠客歐尼爾是否過重：True\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}