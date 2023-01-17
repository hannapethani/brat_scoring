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

TYPE_EMPLOY_             = 'type_employ'
TYPE_EMPLOY_ATTR_        = 'type_employ_attr'

TYPE_HOUSING_            = 'type_housing'
TYPE_HOUSING_ATTR_       = 'type_housing_attr'

LABELED_ARGUMENTS = [STATUS_TIME_, TYPE_EMPLOY_, TYPE_HOUSING_]

# Span only - new
TYPE        = 'Type'
METHOD      = 'Method'
DOSE        = 'Dose'
FREQUENCY   = 'Frequency'
DURATION    = 'Duration'
# HISTORY     = 'History'

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
INPATIENT        = 'inpatient'
PRISON           = 'prison'
HOMELESS         = 'homeless'
