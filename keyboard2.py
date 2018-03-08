major_scales = {"C": ["C", "D", "E", "F", "G", "A", "B"],
                "C#": ["C#", "Eb", "F", "F#", "Ab", "Bb", "C"],
                "D": ["D", "E", "F#", "G", "A", "B", "C#"],
                "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
                "D#": ["D#", "F", "G", "Ab", "Bb", "C", "D"],
                "E": ["E", "F#", "Ab", "A", "B", "C#", "Eb"],
                "F": ["F", "G", "A", "Bb", "C", "D", "E"],
                "F#": ["F#", "Ab", "Bb", "B", "C#", "Eb", "F"],
                "G": ["G", "A", "B", "C", "D", "E", "F#"],
                "Ab": ["Ab", "Bb", "C", "C#", "Eb", "F", "G"],
                "G#": ["G#", "Bb", "C", "C#", "Eb", "F", "G"],
                "A": ["A", "B", "C#", "D", "E", "F#", "Ab"],
                "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"],
                "A#": ["A#", "C", "D", "Eb", "F", "G", "A"],
                "B": ["B", "C#", "Eb", "E", "F#", "Ab", "Bb"]}

minor_scales = {"A": ["A", "B", "C", "D", "E", "F", "G"],
                "Bb": ["Bb", "C", "C#", "Eb", "F", "F#", "Ab"],
                "A#": ["A#", "C", "C#", "D#", "F", "F#", "G#"],
                "B": ["B", "C#", "D", "E", "F#", "G", "A"],
                "C": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
                "C#": ["C#", "Eb", "E", "F#", "Ab", "A", "B"],
                "D": ["D", "E", "F", "G", "A", "Bb", "C"],
                "Eb": ["Eb", "F", "F#", "Ab", "Bb", "B", "C#"],
                "D#": ["D#", "F", "F#", "G#", "A#", "B", "C#"],
                "E": ["E", "F#", "G", "A", "B", "C", "D"],
                "F": ["F", "G", "Ab", "Bb", "C", "C#", "Eb"],
                "F#": ["F#", "Ab", "A", "B", "C#", "D", "E"],
                "G": ["G", "A", "Bb", "C", "D", "Eb", "F"],
                "Ab": ["Ab", "Bb", "B", "C#", "Eb", "E", "F#"],
                "G#": ["G#", "A#", "B", "C#", "D#", "E", "F#"]}
while True:
    try:
        note = str(input("\nPlease type the note you want to see a scale of: ")).strip().upper()
        if note in "QUIT":
            break
        elif note not in major_scales and (len(note) > 1 and note[1] == "B"):
            note_list = list(note)
            note_list[1] = "b"
            note = "".join(note_list)
        major_scale = major_scales[note]
        minor_scale = minor_scales[note]
        print("")
        minor = str(input("Do you want a natural minor scale? [Yes] or [No]")).strip().upper()
        if minor in "NO":
            print(f"The major scale based on key of {note} is: \n{major_scale}\n")
            print(f"The main chords available to play a song in {note} major are: ")
            for scale_note in major_scale:
                if scale_note == major_scale[1] or scale_note == major_scale[2] or scale_note == major_scale[5]:
                    scale_note += "m"
                elif scale_note == major_scale[6]:
                        scale_note += "dim"
                print(scale_note, end="  ")
        elif minor in "YES":
            print(f"The minor scale based on key of {note} is: \n{minor_scale}\n")
            print(f"The main chords available to play a song in {note} minor are: ")
            for scale_note in minor_scale:
                if scale_note == minor_scale[0] or scale_note == minor_scale[3] or scale_note == minor_scale[4]:
                    scale_note += "m"
                elif scale_note == major_scale[1]:
                        scale_note += "dim"
                print(scale_note, end="  ")
        elif minor in "QUIT":
            break
        print("")
    except KeyError:
        print("You must type a valid note!!")
