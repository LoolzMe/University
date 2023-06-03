/* File:      copy.h
   Date:      12/28/01 (written fall 2001)
   Author:    C. Paciorek
   Purpose:   template code for vector copying; contains code because of
              issues with linking when using templates
   Compile:   do not compile this file - merely #include it your code files
   Usage:     
   Arguments: 
   Requires:  
   Reference: 
*/


template<class T1,class T2>
void copy(int len,T1 *vec1,T2 *vec2)
{
  for(int i=0;i<len;i++)
    {
      vec2[i]=(T2) vec1[i];
    }
}



