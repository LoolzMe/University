/* File:      mat_pp.h
   Date:      9/20/01
   Author:    C. Paciorek
   Purpose:   Template code for matrices/2-d arrays stored as vector of pointers to type <T>
              member functions also in this file because of issues with linking when using templates
   Compile:   do not compile this file - merely #include it your code files
   Usage:     
   Arguments:
   Requires:
   Reference:
*/

/* constants used in reading in data */
const int BY_ROW=1;
const int BY_COL=2;
const int RAGGED=1;
const int MATRIX=2;

const int ROW=0;
const int COL=1;


/* constants for specifying warning information */
const int NAN=1;
const int NON_INTEGER=2;
const int LINE_WRONG_LENGTH=3;
const int WRONG_NUMBER_VALUES=4;
const int WRONG_NUMBER_LINES=5;
const int TOO_BIG=6;
const int INDEX_TOO_LARGE=7;

const int SIZE=160000000;
const int DOUBLE_SIZE=8;

template<class T>
class mat_pp {
public:
  mat_pp(int ptr_len_in,int vec_len_in);
  ~mat_pp(void);
  void read(string input_fn,int orient,int format);
  void warn(int line,int value,int warning);
  T* getvec(int index,int rowcol);    /* returns 1-dim vector */
  void getvec(int index,int rowcol,T** output);    /* returns 1-dim vector */
  friend ostream& operator<<<T>(ostream& stream,mat_pp<T>* this_mat_pp);
  T **vals;                           /* public so there is general access to data */
private:
  int ptr_len;                        /* number of rows */
  int vec_len;                        /* number of columns */
  string input_fn;                     /* input filename */
};

/*
template<class T>
ostream& operator<<(ostream& stream,mat_pp<T>* this_mat_pp);
*/

/* note that once I have a compiler that supports the export keyword, I can go back to having separate .h and .C files, with the above declaration of operator << and everything below here in the .C file. */

template<class T>
ostream& operator<<(ostream& stream,mat_pp<T>* this_mat_pp)
{
  /* outputs matrix with one line per row */ 

  int i,j;
  for(i=0;i<this_mat_pp->ptr_len;i++)
    {
      for(j=0;j<this_mat_pp->vec_len;j++)
	{
	  stream << this_mat_pp->vals[i][j] << " "; 
	}
      stream << endl;
    }
  stream << endl;
  return(stream);
}

  

template<class T>
mat_pp<T>::mat_pp(int ptr_len_in,int vec_len_in) {
  int i;
  ptr_len=ptr_len_in;
  vec_len=vec_len_in;
  if(vec_len*ptr_len*DOUBLE_SIZE>SIZE){
    /* cout << vec_len << " " << ptr_len << " " << SIZE << endl; */
    mat_pp::warn(0,0,TOO_BIG);
  }
  else{  
    vals=new (T*)[ptr_len];
    for(i=0;i<ptr_len;i++)
      {
	vals[i]=new T[vec_len];
      }
  }
}

template<class T>
mat_pp<T>::~mat_pp(void)
{
  int i;
  for(i=0;i<ptr_len;i++)
    {
      delete [] vals[i];
    }
  delete [] vals; 
}

template<class T>
T* mat_pp<T>::getvec(int index,int rowcol){
  /* returns array of row or column indicated */

  T* tmp;
  int i;
  if(rowcol==ROW){
    if(index<ptr_len){
      tmp = new T[vec_len];
      for(i=0;i<vec_len;i++){
	tmp[i]=vals[index][i];
      }
    }
    else{
      warn(index,0,INDEX_TOO_LARGE);
    }
  }
  else{
    if(index<vec_len){
      tmp = new T[ptr_len];
      for(i=0;i<ptr_len;i++){
	tmp[i]=vals[i][index];
      }
    }
    else{
      warn(index,0,INDEX_TOO_LARGE);
    }
  }
  return(tmp);
}

template<class T>
void mat_pp<T>::getvec(int index,int rowcol,T** output){
  /* returns array of row or column indicated */
  int i;
  if(rowcol==ROW){
    if(index<ptr_len){
      (*output) = new T[vec_len];
      for(i=0;i<vec_len;i++){
	(*output)[i]=vals[index][i];
      }
    }
    else{
      warn(index,0,INDEX_TOO_LARGE);
    }
  }
  else{
    if(index<vec_len){
      *output = new T[ptr_len];
      for(i=0;i<ptr_len;i++){
	(*output)[i]=vals[i][index];
      }
    }
    else{
      warn(index,0,INDEX_TOO_LARGE);
    }
  }
}

template<class T>
void mat_pp<T>::read(string input_fn,int orient,int format)
{
  /* reads data from input file as determined by orient and format */

  char *linehold = new char[SIZE];
  int line,incr,nonint,i,j,cnt,len;
  int *row; int *col; int* rowlen; int* collen;
  T *tmpvals = new T[vec_len*ptr_len+1];
  int *rowlengths=new int[vec_len*ptr_len+1];

  mat_pp::input_fn=input_fn;
  ifstream input(input_fn.c_str());
  if (input.fail()) 
    {
      cerr << "Error opening file: " << input_fn << endl;
    }
  line=0;
  nonint=0;
  cnt=0;

  /* read data from file into temporary storage */
  while(!input.eof())
    {
      input.getline(linehold,SIZE);
      istrstream buffer(linehold);
      incr=0;
      while(!buffer.fail())
	{
	  buffer >> tmpvals[cnt];
	  if(!buffer.fail()) {incr++; cnt++;}      /* do not increment if nothing read */
	}
      rowlengths[line]=incr;
      if(rowlengths[line]) {line++;}               /* ignore rows in input file with no data */

      /*  check for non-numbers: we must have {-}{#}{.}{#} */
      len=strlen(linehold);
      for(i=0;i<len;i++)
	{
	  if(! (isdigit(linehold[i]) || isspace(linehold[i])) )
	    {
	      if(! (
		 (linehold[i]=='-' && (isdigit(linehold[i+1]) || linehold[i]=='.') && (i==0 || isspace(linehold[i-1]))) ||
		 (linehold[i]=='.' && (isdigit(linehold[i+1])) &&
		  (i==0 || isdigit(linehold[i-1]) || isspace(linehold[i-1]) || linehold[i-1]=='-'))
		 ) ){
		mat_pp::warn(line,0,NAN);          
		}
	      if(linehold[i]=='.') {nonint=1;}     /* we have detected a floating point */
	    }
	}
    }


  /* give warnings as necessary */
  if(nonint){
    mat_pp::warn(0,0,NON_INTEGER);  /* warn if floating points detected; not sure how to check type of T so that irrelevant warnings not given */
  }
  if(format==MATRIX) {  /* check that input file is of proper dimension */
    if((orient==BY_ROW && line!=ptr_len) || (orient==BY_COL && line!=vec_len)) {
      mat_pp::warn(0,line,WRONG_NUMBER_LINES);
    }   /* number of lines wrong */
    for(i=0;i<line;i++) {
      if(rowlengths[i] && (orient==BY_ROW && rowlengths[i]!=vec_len) || (orient==BY_COL && rowlengths[i]!=ptr_len)) {
	mat_pp::warn(i+1,rowlengths[i],LINE_WRONG_LENGTH);
      }  /* row lengths wrong */
    }
  }
  if(format==RAGGED){  /* only need check total number of values */
    if(cnt!=vec_len*ptr_len){
      mat_pp::warn(0,cnt,WRONG_NUMBER_VALUES);
    }  /* total number of values wrong */
  }

  /* move values from temp storage to matrix */
  if(orient==BY_ROW){
    row=&i; col=&j; rowlen=&ptr_len; collen=&vec_len;
  }
  else{
    row=&j; col=&i; rowlen=&vec_len; collen=&ptr_len;
  }
  cnt=0; i=0;
  while(i<*rowlen){
    j=0;
    while(j<*collen){
      vals[*row][*col]=tmpvals[cnt];
      cnt++; j++;
    }
    i++;
  }

  delete [] linehold;
  delete [] tmpvals;
  delete [] rowlengths;
}

template<class T>
void mat_pp<T>::warn(int line,int value,int warn)
{
  if(warn == NAN){
    cerr << "Warning: there is a non-number in " << mat_pp::input_fn << ", line " << line <<".\n";
  }
  if(warn == NON_INTEGER){
    cerr << "Warning: data " << mat_pp::input_fn << " are not integer-valued.\n";
  }
  if(warn == WRONG_NUMBER_LINES){
    cerr << "Warning: found " << value << " lines in " << mat_pp::input_fn << "; this does not match the number expected.\n";
  }
  if(warn == LINE_WRONG_LENGTH){
    cerr << "Warning: line " << line << " has " << value << " values in " << mat_pp::input_fn << "; this does not match the number expected.\n";
  }
  if(warn == WRONG_NUMBER_VALUES){
    cerr << "Warning: there are " << value << " values in " << mat_pp::input_fn << "; this does not match the number expected.\n";
  }
  if(warn==TOO_BIG){
    cerr << "Need to allocate more space in temporary storage in mat_pp read function\n";
  }
  if(warn==INDEX_TOO_LARGE){
    cerr << "Index " << line << " exceeds number of rows or columns\n";
  }
}










