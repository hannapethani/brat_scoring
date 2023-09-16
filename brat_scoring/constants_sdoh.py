'''
Determinants
'''

TOBACCO         = 'Tobacco'
ALCOHOL         = 'Alcohol'
METHAMPHETAMINE = 'Methamphetamine'
SUGAR           = 'Sugar'

EMPLOYMENT      = 'Employment'
HOUSING         = 'Housing'


'''
Entities
'''

TRIGGER = 'Trigger'

STATUS  = 'Status'


# Span and class - new
STATUS_TIME              = 'status_time'
STATUS_TIME_ATTR        = 'status_time_attr'

STATUS_EMPLOY           = 'status_employ'
STATUS_EMPLOY_ATTR      = 'status_employ_attr'

STATUS_HOUSING          = 'status_housing'
STATUS_HOUSING_ATTR     = 'status_housing_attr'


# Span only - new
TYPE        = 'Type'
METHOD      = 'Method'
DOSE        = 'Dose'
FREQUENCY   = 'Frequency'
DURATION    = 'Duration'
HISTORY     = 'History'

NONE    = 'none'
CURRENT = 'current'
PAST    = 'past'
FUTURE  = 'future'

# employment types
EMPLOYED      = 'employed'
UNEMPLOYED    = 'unemployed'
RETIRED       = 'retired'
ON_DISABILITY = 'on_disability'
STUDENT       = 'student'
HOMEMAKER     = 'homemaker'

# housing types
PRIVATE          = 'private'
SOCIAL_HOUSING   = 'social_housing'
OUT_OF_HOME_CARE = 'out_of_home_care'
PRISON           = 'prison'
HOMELESS         = 'homeless'

LABELED_ARGUMENTS = [STATUS_TIME, STATUS_EMPLOY, STATUS_HOUSING]
SPAN_ONLY_ARGUMENTS = [DOSE, DURATION, FREQUENCY, HISTORY, METHOD, TYPE]
