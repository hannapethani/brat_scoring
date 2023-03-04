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
STATUS_TIME_             = 'status_time'
STATUS_TIME_ATTR_        = 'status_time_attr'

STATUS_EMPLOY_           = 'status_employ'
STATUS_EMPLOY_ATTR_      = 'status_employ_attr'

STATUS_HOUSING_          = 'status_housing'
STATUS_HOUSING_ATTR_     = 'status_housing_attr'


# Span only - new
TYPE        = 'Type'
METHOD      = 'Method'
DOSE        = 'Dose'
FREQUENCY   = 'Frequency'
DURATION    = 'Duration'
HISTORY     = 'History'
LIVES_WITH  = 'Lives_With'

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

LABELED_ARGUMENTS = [STATUS_TIME_, STATUS_EMPLOY_, STATUS_HOUSING_]
SPAN_ONLY_ARGUMENTS = [DOSE, DURATION, FREQUENCY, HISTORY, METHOD, TYPE]
