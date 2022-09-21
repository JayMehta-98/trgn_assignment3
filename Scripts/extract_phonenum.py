{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "1fefa32b-5a62-4a55-b542-0c9eb299e41e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My phone number in England was +44-20-7183-8750, and now that I moved to Arizona, it is 480-448-0157.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import re \n",
    "with open('mytextfile.txt') as f:\n",
    "    contents = f.read()\n",
    "print (contents)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "8d06fb7b-7e7d-4958-ab40-9ca5ec8e984b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "phone number : ['+44-20-7183-8750', '+1-480-448-0157']\n"
     ]
    }
   ],
   "source": [
    "match = re.findall(r'[\\+\\]?[0-9][0-9 .\\-\\(\\)]{8,}[0-9]', contents)\n",
    "if match:\n",
    "    print ('phone number :', match)\n",
    "\n",
    "else:\n",
    "    print ('No match')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "60307af7-5144-43a8-8fb6-b5eb5ee8df4b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['+1', '480', '448', '0157']"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "d684e0b9-523d-4262-9dce-a382e38e64e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['+44-20-7183-8750', '+1-480-448-0157']"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "match"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "c46a1ecc-3d79-427c-a777-635365ad70c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "s = match[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "f9017274-2779-4af2-9511-930b33931e72",
   "metadata": {},
   "outputs": [],
   "source": [
    "if s.split(\"-\")[0]==\"+1\":\n",
    "    # print(\"Domestic\")\n",
    "        l = s.split(\"-\")\n",
    "        res =[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "bf9d32d6-f7c1-4bc5-8f24-a6c278c676d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+44(20)71838750\n",
      "+1(480)4480157\n"
     ]
    }
   ],
   "source": [
    "for s in match:\n",
    "    if s.split(\"-\")[0]==\"+1\":\n",
    "    # print(\"Domestic\")\n",
    "        l = s.split(\"-\")\n",
    "        res =[]\n",
    "        for i in range(len(l)):\n",
    "            if i==1:\n",
    "                res.append(\"(\")\n",
    "                res.append(l[i])\n",
    "            elif i==2:\n",
    "                res.append(\")\")\n",
    "                res.append(l[i])\n",
    "            else:\n",
    "                res.append(l[i])\n",
    "        final_format = \"\".join(map(str, res))\n",
    "    else:\n",
    "        # print(\"International\")\n",
    "        l = s.split(\"-\")\n",
    "        res =[]\n",
    "        for i in range(len(l)):\n",
    "            if i==1:\n",
    "                res.append(\"(\")\n",
    "                res.append(l[i])\n",
    "            elif i==2:\n",
    "                res.append(\")\")\n",
    "                res.append(l[i])\n",
    "            else:\n",
    "                res.append(l[i])\n",
    "        final_format = \"\".join(map(str, res))\n",
    "    print(final_format)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "2fb63219-48a7-4d45-8373-202ad04509f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "d9601eb7-9f16-40f5-93a2-3fa8b24ac7d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'+44-20-7183-8750'"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# match[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "3bc3898d-6287-4b97-bc35-d6291925abf4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# s=match[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "9de2b729-cc42-4418-adf6-41b06c736ceb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'+44-20-7183-8750'"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "221dc4e5-2565-449d-86a4-a2da5ab1185e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# l = s.split(\"-\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "4406d857-3165-4747-b13e-bbcbfb1a3acb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['+44', '20', '7183', '8750']"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "bd34810d-0285-4623-a158-30c9d5f79560",
   "metadata": {},
   "outputs": [],
   "source": [
    "# res =[]\n",
    "# for i in range(len(l)):\n",
    "#     if i==1:\n",
    "#         res.append(\"(\")\n",
    "#         res.append(l[i])\n",
    "#     elif i==2:\n",
    "#         res.append(\")\")\n",
    "#         res.append(l[i])\n",
    "#     else:\n",
    "#         res.append(l[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "981ead2a-0489-435c-b710-69342697cee2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['+44', '(', '20', ')', '7183', '8750']"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "1ce922a0-16af-42fa-a898-8ccce10cee44",
   "metadata": {},
   "outputs": [],
   "source": [
    "# final_format = \"\".join(map(str, res))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "7373db37-9161-483b-9b48-57dea003505d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'+44(20)71838750'"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# final_format"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
