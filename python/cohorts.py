#cohort profiles
atl_program = {
  'city':'atlanta',
  'status':'ongoing',
  'enrolled':69
}
dmv_program = {
  'city': 'dmv',
  'status':'ongoing',
  'enrolled':54
}
ny_nj_program = {
  'city':'ny_nj',
  'status':'renewal',
  'enrolled':84
}
la_program = {
  'city': 'los_angeles',
  'status':'renewal',
  'enrolled':75
}
kc_program = {
  'city': 'kansas_city',
  'status':'pilot',
  'enrolled':0
  }

print(kc_program['status'])
print(la_program['enrolled'])

print(dmv_program.keys())
print(dmv_program.values())
print(dmv_program.items())

