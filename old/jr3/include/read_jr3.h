#ifndef _READ_JR3
#define _READ_JR3


#define DATA_LEN 18
#define NUM_AXES 3
#define OFFSET_S1 0
#define OFFSET_S2 9
#define OFFSET_FORCE 0
#define OFFSET_MOMENT 3
#define OFFSET_SAFE 6

#define SPEC_A 470
#define SPEC_B 600
#define SPEC_C 490
#define SPEC_D 1900
#define SPEC_E 40
#define SPEC_F 105
#define SPEC_G 28
#define SPEC_H 22

#ifdef __cplusplus
extern "C" void read_global(float * values);
extern "C" void init(void);
#else
void read_global(float * values);
void init(void);
#endif

#endif
