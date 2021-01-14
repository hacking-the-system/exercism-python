def recite(start_verse, end_verse):
    number_ordinal = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    first_stanza = "On the " + number_ordinal[start_verse] + " day of Christmas my true love gave to me: "
    song = first_stanza

    stanzas = {
        2: "two Turtle Doves",
        3: "three French Hens",
        4: "four Calling Birds",
        5: "five Gold Rings",
        6: "six Geese-a-Laying",
        7: "seven Swans-a-Swimming",
        8: "eight Maids-a-Milking",
        9: "nine Ladies Dancing",
        10: "ten Lords-a-Leaping",
        11: "eleven Pipers Piping",
        12: "twelve Drummers Drumming"
    }

    if end_verse > 1:
        for i in range(end_verse, 1, -1):
            song += stanzas[i]
            song += ", " if i > 2 else ", and "
    
    last_stanza = "a Partridge in a Pear Tree."
    song += last_stanza
    return [song]
