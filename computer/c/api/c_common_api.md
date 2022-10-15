# C 语言常用 API

- pthread

  ```c
  #include <pthread.h>

  int pthread_create(pthread_t *restrict tidp,
                     const pthread_attr_t *restrict attr,
                     void *(*start_rtn)(void *), void *restrict arg);

  int pthread_join(pthread_t thread, void **rval_ptr);

  // Both Returns: 0 if OK, error number on failure

  void pthread_exit(void *rval_ptr);
  ```

- pthread mutex

  ```c

  #include <pthread.h>

  int pthread_mutex_init(pthread_mutex_t *restrict mutex,
                         const pthread_mutexattr_t *restrict attr);

  int pthread_mutex_lock(pthread_mutex_t *mutex);
  int pthread_mutex_trylock(pthread_mutex_t *mutex);
  int pthread_mutex_unlock(pthread_mutex_t *mutex);
  int pthread_mutex_destroy(pthread_mutex_t *mutex);

  // All return: 0 if OK, error number on failure
  ```

- semaphore

  ```c
  #include <semaphore.h>

  int sem_init(sem_t *sem, int pshared, unsigned int value);
  int sem_wait(sem_t *sem);
  int sem_post(sem_t *sem);
  int sem_destroy(sem_t *sem);

  // All Returns 0 on success; on error, -1 is returned, and errno is set to indicate the error.
  ```

- sleep vs usleep

  ```c
  #include <unistd.h>

  // sleep for a specified number of seconds.
  // Returns 0 if the requested time has elapsed,
  // or the number of seconds left to sleep, if the call was interrupted by a signal handler.
  unsigned int sleep(unsigned int seconds);

  // suspend execution for microsecond intervals.
  // Returns 0 on success. On error, -1 is returned, with errno set to indicate the cause of the error.
  int usleep(useconds_t usec);
  ```

- rand vs srand

  ```c
  #include <stdlib.h>

  // Sets its argument as the seed for a new sequence of pseudo-random integers to be returned by rand().
  void srand(unsigned int seed);

  // Returns a pseudo-random integer in the range 0 to RAND_MAX inclusive.
  int rand(void);
  ```

- time

  ```c
  #include <time.h>

  // Returns the time as the number of seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC).
  // If tloc is non-NULL, the return value is also stored in the memory pointed to by tloc.
  time_t time(time_t *tloc);
  ```
