'''
Determinants
'''

TOBACCO = 'Tobacco'
ALCOHOL = 'Alcohol'
METHAMPHETAMINE = 'Methamphetamine'
SUGAR = 'Sugar'

EMPLOYMENT = 'Employment'
HOUSING = 'Housing'

# COUNTRY = 'Country'
# DRUG = 'Drug'
# ENVIRO_EXPOSURE = 'EnviroExposure'
# GENDER_ID = 'GenderID'
# INSURANCE = 'Insurance'
# LIVING_STATUS = 'LivingStatus'
# PHYS_ACTIVITY = 'PhysActivity'
# RACE = 'Race'
# SEXUAL_ORIENT = 'SexualOrient'


'''
Entities
'''

TRIGGER = 'Trigger'

STATUS                  = 'Status'


# Span and class - new
STATUS_TIME             = 'StatusTime'
STATUS_TIME_VAL         = 'StatusTimeVal'

STATUS_EMPLOY           = 'StatusEmploy'
STATUS_EMPLOY_VAL       = 'StatusEmployVal'

TYPE_HOUSING             = 'TypeHousing'
TYPE_HOUSING_VAL         = 'TypeHousingVal'

LABELED_ARGUMENTS = [STATUS_TIME, STATUS_EMPLOY, TYPE_HOUSING]

# Span only - new
TYPE        = 'Type'
METHOD      = 'Method'
DOSE        = 'Dose'
FREQUENCY   = 'Frequency'
DURATION    = 'Duration'
# HISTORY     = 'History'

CURRENT = 'current'
PAST = 'past'
FUTURE = 'future'

# employment types
EMPLOYED = 'employed'
UNEMPLOYED = 'unemployed'
RETIRED = 'retired'
ON_DISABILITY = 'on_disability'
STUDENT = 'student'
HOMEMAKER = 'homemaker'

# housing types
PRIVATE = 'private'
SOCIAL_HOUSING = 'social_housing'
OUT_OF_HOME_CARE = 'out_of_home_care'
INPATIENT = 'inpatient'
PRISON = 'prison'
HOMELESS = 'homeless'
