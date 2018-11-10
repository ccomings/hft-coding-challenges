#lang racket

(define (lists-same? a b) (equal? (list->set a) (list->set b)))

(define (n-sum nums count goal)
  (remove-duplicates
   (filter-map
    (lambda (xs) (and (= goal (apply + xs)) xs))
    (combinations nums count))
   lists-same?))


(n-sum '(-1 0 1 2 -1 -4) 3 0)

(n-sum '(-2 3 0 1 1 -1) 3 0)

(n-sum '(1 2 3 4) 3 0)

(n-sum '(1 2 3) 3 6)
