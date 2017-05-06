#include <stdlib.h>
//from linux kernel 2.6.32 , C style: --std=c99 or later (not ok on c89)

/* Force a compilation error if condition is true */
#define BUILD_BUG_ON(condition) ((void)BUILD_BUG_ON_ZERO(condition))

/* Force a compilation error if condition is constant and true */
// note it not work if condition has variable!
#define MAYBE_BUILD_BUG_ON(cond) ((void)sizeof(char[1 - 2 * !!(cond)]))

/* Force a compilation error if condition is true, but also produce a
   result (of value 0 and type size_t), so the expression can be used
   e.g. in a structure initializer (or where-ever else comma expressions
   aren't permitted). */
#define BUILD_BUG_ON_ZERO(e) (sizeof(struct { int:-!!(e); }))
//eg:
//a=1;MAYBE_BUILD_BUG_ON(a!=2); //not work
//BUILD_BUG_ON(1!=2); // work!