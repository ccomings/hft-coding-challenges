#lang racket

(define (lists-same? a b) (equal? (list->set a) (list->set b)))

(define (n-sum nums count goal)
  (remove-duplicates
   (filter-map
    (lambda (xs) (and (= goal (apply + xs)) xs))
    (combinations nums count))
   lists-same?))

(define (3-sum nums)
  (n-sum nums 3 0))

;; These should be the same:
(n-sum '(-1 0 1 2 -1 -4) 3 0)
(3-sum '(-1 0 1 2 -1 -4))

;; Some more 3-sums
(3-sum '(-2 3 0 1 1 -1))
(3-sum '(1 2 3 4))

;; find triples that add up to 6
(n-sum '(0 1 2 3 4 5 6) 3 6)
