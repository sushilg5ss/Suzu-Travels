LEH = [("January","1.5° / −13.1 °C"),("February","4.2° / −9.2 °C"),("March","9.7° / −3.7 °C"),("April","15.3° / 1.6 °C"),("May","20.0° / 6.2 °C"),("June","24.4° / 11.3 °C"),("July","28.5° / 15.9 °C"),("August","28.1° / 15.1 °C"),("September","23.4° / 9.2 °C"),("October","16.7° / 0.3 °C"),("November","10.6° / −7.2 °C"),("December","4.5° / −11.7 °C")]
def rows(notes):
    return [[m, t, n] for (m, t), n in zip(LEH, notes)]
