/* File:      base.h
   Date:      6/22/02 (written fall 2001)
   Author:    C. Paciorek
   Purpose:   general header info for Bayesian GP spatial model
              has all the include files for the whole program
   Compile:   
   Usage:     
   Arguments: 
   Requires:  mat_pp.h,copy.h
   Reference: 
*/

#include <fstream>
#include <iostream>
#include <iomanip>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <strstream>
#include <string>
#include <iostream>
#include <math.h>
#include <stddef.h>
#include <unistd.h>
#include <ctime>

#include "mat_pp.h"  /* general storage code */
#include "copy.h"   /* templates for vector copying */
#include "generic_functions.h"

#define GMT_d_NaN
/* #define VECTOR_DOUBLE_BOUNDS_CHECK */

const double ERROR=-9.0;

const double SMALL=0.000001;

const int TRUE=1;
const int FALSE=0;

const int FIRST=1;
const int NOT_FIRST=0;

const int STATIONARY=0;
const int NON_STATIONARY=2;
/* FIXED is defined further down to be 1 */

const int CONSTANT=0;
const int VARIABLE=1;

const double PI=3.14159265358979323846;
const double PI_2=1.57079632679489661923;
const double TWO_PI=2*3.14159265358979323846;
const double SQRT2=sqrt(2);

/* number of geographic locations */
const int LOCN=133; /*3024; */
const int LAT=7; /*21;*/
const int LON=19; /*144;*/
const int YEAR=51;

const int ACCEPT=1;
const int REJECT=0;

/* which units to use */
const int RADIANS=1;
const int DEGREES=2;
const int MM=3;
const int KM=4;

/* SI length conversions */
const double M2MM=.000001;
const double M2KM=.001;
const double KM2M=1000.0;
const double KM2MM=.001;
const double MM2M=1000000.0;
const double MM2KM=1000.0;

/* degrees to radians and back */
const double D2R=0.0174533; /* PI/180 */
const double R2D= 57.2958;  /* 180/PI */

/* indicate which parameter an object instatiation is */
const int ALPHA=1;
const int BETA=2;
const int ETA=3;
const int DELTA=4;
const int DATA_KAPPA=5;
const int DATA_COVAR_EIGVAL=6;
const int DATA_COVAR_EIGVEC=7;
const int DATA_EIG_KAPPA=8;
const int LANG=9;
const int NU=10;

const int SIMPLE=0;
const int POSTMEAN=1;
const int NON_LANGEVIN=0;
const int LANGEVIN=1;
const int JOINT_THETA=0;
const int JOINT_AND_INDIV_THETA=1;

const int FIXED=1;
const int NOT_FIXED=0;

const int CURRENT=0;
const int FINAL=1;

const int WARN=1;
const int NO_WARN=0;

const int THETA_NOREP=2;
const int THETA_REP=1;
const int KSI_NOREP=0;

const int GENERATE=0;
const int WRITE=1;
const int READ=2;

/* equatorial radius stuff */

/*http://ssd.jpl.nasa.gov/phys_props_earth.html
EQUATORIAL RADIUS, a
  (IAU,1976)                           6378140 m
  (Geod. ref. sys., 1980)              6378137 m
  (Merit,1983)                         6378136 m
*/

/* I define this directly rather than using the whole structure of GMT */
/*#define EQ_RADIUS  6378140  */ /* from the web - see above */
/*#define EQ_RADIUS  6378137 */  /* WGS-84 from GMT defaults */

const double EQ_RADIUS=6371008.7714;   /* sphere from GMT defaults - this is used in project */











