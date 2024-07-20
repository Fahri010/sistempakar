import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def fuzzy_logic(data):
    # Definisikan semua 30 ciri-ciri gaya belajar sebagai variabel input
    parameters = [
        "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09",
        "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18",
        "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27",
        "C28", "C29", "C30"
    ]

    # Membuat variabel input
    antecedents = {}
    for param in parameters:
        antecedents[param] = ctrl.Antecedent(np.arange(0, 101, 1), param)
        antecedents[param]['jarang'] = fuzz.trimf(antecedents[param].universe, [0, 0, 40])
        antecedents[param]['kadang'] = fuzz.trimf(antecedents[param].universe, [20, 40, 60])
        antecedents[param]['sering'] = fuzz.trimf(antecedents[param].universe, [40, 60, 80])
        antecedents[param]['sangat_sering'] = fuzz.trimf(antecedents[param].universe, [60, 80, 100])

    # Membuat variabel output
    learning_style = ctrl.Consequent(np.arange(0, 101, 1), 'learning_style')
    learning_style['visual'] = fuzz.trimf(learning_style.universe, [0, 0, 50])
    learning_style['auditory'] = fuzz.trimf(learning_style.universe, [0, 50, 100])
    learning_style['kinesthetic'] = fuzz.trimf(learning_style.universe, [50, 100, 100])

    # Membuat aturan
    rules = []

    # Mengkonversi kombinasi fuzzy ke aturan
    # def create_rule(variables, output, style):
    #     rule = None
    #     if len(variables) == 3:
    #         rule = ctrl.Rule(
    #             antecedents[variables[0]][output] &
    #             antecedents[variables[1]][output] &
    #             antecedents[variables[2]][output],
    #             learning_style[style]
    #         )
    #     elif len(variables) == 2:
    #         rule = ctrl.Rule(
    #             antecedents[variables[0]][output] &
    #             antecedents[variables[1]][output],
    #             learning_style[style]
    #         )
    #     elif len(variables) == 1:
    #         rule = ctrl.Rule(
    #             antecedents[variables[0]][output],
    #             learning_style[style]
    #         )
    #     if rule:
    #         rules.append(rule)
            
    # # Visual
    # create_rule(["C01", "C04", "C07"], 'sering', 'visual')
    # create_rule(["C10", "C13", "C16"], 'sering', 'visual')
    # create_rule(["C19", "C22", "C25"], 'sering', 'visual')
    # create_rule(["C28"], 'sering', 'visual')

    # # Auditory
    # create_rule(["C02", "C05", "C08"], 'sering', 'auditory')
    # create_rule(["C11", "C14", "C17"], 'sering', 'auditory')
    # create_rule(["C20", "C23", "C26"], 'sering', 'auditory')
    # create_rule(["C29"], 'sering', 'auditory')

    # # Kinesthetic
    # create_rule(["C03", "C06", "C09"], 'sering', 'kinesthetic')
    # create_rule(["C12", "C15", "C18"], 'sering', 'kinesthetic')
    # create_rule(["C21", "C24", "C27"], 'sering', 'kinesthetic')
    # create_rule(["C30"], 'sering', 'kinesthetic')


    def create_rule(variables, outputs):
        for output in outputs:
            if len(variables) == 3:
                rule = ctrl.Rule(
                    antecedents[variables[0]][output[0]] &
                    antecedents[variables[1]][output[1]] &
                    antecedents[variables[2]][output[2]],
                    learning_style[output[3]]
                )
            elif len(variables) == 2:
                rule = ctrl.Rule(
                    antecedents[variables[0]][output[0]] &
                    antecedents[variables[1]][output[1]],
                    learning_style[output[2]]
                )
            elif len(variables) == 1:
                rule = ctrl.Rule(
                    antecedents[variables[0]][output[0]],
                    learning_style[output[1]]
                )
            rules.append(rule)

    create_rule(["C01", "C04", "C07"], [
        ('sering', 'jarang', 'jarang', 'visual'),
        ('sering', 'sering', 'jarang', 'visual'),
        ('sering', 'sering', 'sering', 'visual'),
        ('jarang', 'jarang', 'sering', 'visual'),
    ])
    create_rule(["C10", "C13", "C16"], [
        ('sering', 'jarang', 'jarang', 'visual'),
        ('sering', 'sering', 'jarang', 'visual'),
        ('sering', 'sering', 'sering', 'visual'),
        ('jarang', 'jarang', 'sering', 'visual'),
    ])
    create_rule(["C19", "C22", "C25"], [
        ('sering', 'jarang', 'jarang', 'visual'),
        ('sering', 'sering', 'jarang', 'visual'),
        ('sering', 'sering', 'sering', 'visual'),
        ('jarang', 'jarang', 'sering', 'visual'),
    ])
    create_rule(["C28"], [
        ('sering', 'visual'),
    ])

    create_rule(["C02", "C05", "C08"], [
        ('sering', 'jarang', 'jarang', 'auditory'),
        ('sering', 'sering', 'jarang', 'auditory'),
        ('sering', 'sering', 'sering', 'auditory'),
        ('jarang', 'jarang', 'sering', 'auditory'),
    ])
    create_rule(["C11", "C14", "C17"], [
        ('sering', 'jarang', 'jarang', 'auditory'),
        ('sering', 'sering', 'jarang', 'auditory'),
        ('sering', 'sering', 'sering', 'auditory'),
        ('jarang', 'jarang', 'sering', 'auditory'),
    ])
    create_rule(["C20", "C23", "C26"], [
        ('sering', 'jarang', 'jarang', 'auditory'),
        ('sering', 'sering', 'jarang', 'auditory'),
        ('sering', 'sering', 'sering', 'auditory'),
        ('jarang', 'jarang', 'sering', 'auditory'),
    ])
    create_rule(["C29"], [
        ('sering', 'auditory'),
    ])

    create_rule(["C03", "C06", "C09"], [
        ('sering', 'jarang', 'jarang', 'kinesthetic'),
        ('sering', 'sering', 'jarang', 'kinesthetic'),
        ('sering', 'sering', 'sering', 'kinesthetic'),
        ('jarang', 'jarang', 'sering', 'kinesthetic'),
    ])
    create_rule(["C12", "C15", "C18"], [
        ('sering', 'jarang', 'jarang', 'kinesthetic'),
        ('sering', 'sering', 'jarang', 'kinesthetic'),
        ('sering', 'sering', 'sering', 'kinesthetic'),
        ('jarang', 'jarang', 'sering', 'kinesthetic'),
    ])
    create_rule(["C21", "C24", "C27"], [
        ('sering', 'jarang', 'jarang', 'kinesthetic'),
        ('sering', 'sering', 'jarang', 'kinesthetic'),
        ('sering', 'sering', 'sering', 'kinesthetic'),
        ('jarang', 'jarang', 'sering', 'kinesthetic'),
    ])
    create_rule(["C30"], [
        ('sering', 'kinesthetic'),
    ])



    # Membuat kontrol sistem
    learning_style_ctrl = ctrl.ControlSystem(rules)
    learning_style_sim = ctrl.ControlSystemSimulation(learning_style_ctrl)

    # Memberikan input nilai
    inputs = data
    print(f"Inputs: {inputs}")  # Logging input values for debugging

    # Memberikan input nilai
    # Misalnya, ini adalah input dari pengguna
    inputs = data

    total_visual = inputs['C01'] + inputs['C04'] + inputs['C07'] + inputs['C10'] + inputs['C13'] + inputs['C16'] + inputs['C19'] + inputs['C22'] + inputs['C25'] + inputs['C28']
    total_auditory = inputs['C02'] + inputs['C05'] + inputs['C08'] + inputs['C11'] + inputs['C14'] + inputs['C17'] + inputs['C20'] + inputs['C23'] + inputs['C26'] + inputs['C29']
    total_kinesthetic = inputs['C03'] + inputs['C06'] + inputs['C09'] + inputs['C12'] + inputs['C15'] + inputs['C18'] + inputs['C21'] + inputs['C24'] + inputs['C27'] + inputs['C30']


    for key, value in inputs.items():
        learning_style_sim.input[key] = value

    # Melakukan perhitungan
    learning_style_sim.compute()

    # Menentukan gaya belajar berdasarkan output
    if learning_style_sim.output['learning_style'] < 50:
        hasil_gaya_belajar = 'Visual'
    elif 50 <= learning_style_sim.output['learning_style'] <= 75:
        hasil_gaya_belajar = 'Auditory'
    else:
        hasil_gaya_belajar = 'Kinesthetic'

    return {
        "total_visual": total_visual,
        "total_auditory": total_auditory,
        "total_kinesthetic": total_kinesthetic,
        "output_value": learning_style_sim.output['learning_style'],
        "learning_style": hasil_gaya_belajar
    }