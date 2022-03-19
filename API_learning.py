{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "API-Homework.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP0uScr4g5IY7GnC1rR9aLq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/risgmf74/Java-Programming/blob/main/API_learning.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Homework - API"
      ],
      "metadata": {
        "id": "LGZFY6VUtVhy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Game of Thrones Characters"
      ],
      "metadata": {
        "id": "t502DLxqMeQY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import requests\n",
        "import time\n",
        "\n",
        "# Endpoint - Base URL\n",
        "url = \"https://anapioficeandfire.com/api/characters/\"\n",
        "\n",
        "# Request data with get\n",
        "response = requests.get(url)\n",
        "print(response)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "46m-5xONtdSU",
        "outputId": "2bd2dd61-5871-4667-eeac-9f9085e1209f"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<Response [200]>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Get character name, From 1 to 2137 characters\n",
        "# Jon Snow is at 583\n",
        "\n",
        "characters_list = []\n",
        "\n",
        "def getCharacter():\n",
        "\n",
        "  print(\"Enter your value (Numbers must between 1 to 2137)\")\n",
        "  start = int(input(\"Start: \"))\n",
        "  end = int(input(\"End: \"))\n",
        "\n",
        "  for i in range(start, end):\n",
        "    new_url = url + str(i)\n",
        "    response = requests.get(new_url)\n",
        "    response_json = response.json() \n",
        "    data = [\n",
        "        response_json['name'],\n",
        "        response_json['gender'],\n",
        "        response_json['culture'],\n",
        "        response_json['died'],\n",
        "        response_json['titles']\n",
        "    ]\n",
        "    characters_list.append(data)\n",
        "    time.sleep(2)\n",
        "\n",
        "  print(characters_list)"
      ],
      "metadata": {
        "id": "O2-YFpqduDk5"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Call getCharacter function\n",
        "getCharacter()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KQV_qBlQ2fe4",
        "outputId": "2da0ca40-cbf8-4755-8b40-64efef522d36"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your value (Numbers must between 1 to 2137)\n",
            "Start: 583\n",
            "End: 598\n",
            "[['Jon Snow', 'Male', 'Northmen', '', [\"Lord Commander of the Night's Watch\"]], ['Jon Stark', 'Male', '', '', ['King in the North']], ['Jon Umber', 'Male', 'Northmen', '', ['Lord of the Last Hearth']], ['Jon Umber', 'Male', 'Northmen', 'In 299 AC, at the Twins', ['']], ['Jon Wylde', 'Male', '', '', ['Ser']], ['Jonelle Cerwyn', 'Female', 'Northmen', '', ['Lady of Cerwyn']], ['Jonnel Stark', 'Male', '', '', ['Lord of Winterfell', 'Warden of the North']], ['Jonos Frey', 'Male', '', '', ['']], ['Jonos Stark', 'Male', 'Northmen', '', ['King in the North', 'Lord of Winterfell']], ['Jonothor Darry', 'Male', '', 'In 283 AC, at the Trident', ['Ser']], ['Jorah Stark', 'Male', 'Northmen', '', ['King in the North', 'Lord of Winterfell']], ['Jorelle Mormont', 'Female', 'Northmen', '', ['']], ['Jory Cassel', 'Male', 'Northmen', \"In 298 AC, at King's Landing\", ['Captain of the guard']], ['Joseth Mallister', 'Male', '', '', ['Ser']], ['Josmyn Peckledon', 'Male', '', '', ['']]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Convert result to DataFrame\n",
        "characters_df = pd.DataFrame(characters_list, columns = [\"name\", \"gender\", \"culture\", \"died\", \"titles\"])"
      ],
      "metadata": {
        "id": "zIQm4eLZGY5U"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Call DataFrame\n",
        "characters_df"
      ],
      "metadata": {
        "id": "G-7_vlTgGgMW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Export to csv file\n",
        "characters_df.to_csv(\"characters.csv\", index = False)"
      ],
      "metadata": {
        "id": "KaFy_mLGJM5j"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Filter only who died (Only who died is not empty string)\n",
        "characters_df.query(\" died != ''\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "jnYpDh-GJ627",
        "outputId": "82c50088-5581-45a7-c839-234090d18361"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              name gender   culture                          died  \\\n",
              "3        Jon Umber   Male  Northmen       In 299 AC, at the Twins   \n",
              "9   Jonothor Darry   Male               In 283 AC, at the Trident   \n",
              "12     Jory Cassel   Male  Northmen  In 298 AC, at King's Landing   \n",
              "\n",
              "                    titles  \n",
              "3                       []  \n",
              "9                    [Ser]  \n",
              "12  [Captain of the guard]  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ea258ade-70ef-4175-b97e-c37dc6815b38\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>name</th>\n",
              "      <th>gender</th>\n",
              "      <th>culture</th>\n",
              "      <th>died</th>\n",
              "      <th>titles</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Jon Umber</td>\n",
              "      <td>Male</td>\n",
              "      <td>Northmen</td>\n",
              "      <td>In 299 AC, at the Twins</td>\n",
              "      <td>[]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>Jonothor Darry</td>\n",
              "      <td>Male</td>\n",
              "      <td></td>\n",
              "      <td>In 283 AC, at the Trident</td>\n",
              "      <td>[Ser]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>Jory Cassel</td>\n",
              "      <td>Male</td>\n",
              "      <td>Northmen</td>\n",
              "      <td>In 298 AC, at King's Landing</td>\n",
              "      <td>[Captain of the guard]</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ea258ade-70ef-4175-b97e-c37dc6815b38')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-ea258ade-70ef-4175-b97e-c37dc6815b38 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-ea258ade-70ef-4175-b97e-c37dc6815b38');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    }
  ]
}