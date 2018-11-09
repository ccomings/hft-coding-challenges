#lang racket

(define test-list '(-1 0 1 2 -1 -4))

(define (lists-same? a b) (equal? (list->set a) (list->set b)))

(define (n-sum nums count goal)
  (remove-duplicates
   (filter-map
    (lambda (xs) (and (= goal (apply + xs)) xs))
    (combinations nums count))
   lists-same?))


