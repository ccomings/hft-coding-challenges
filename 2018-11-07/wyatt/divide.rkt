#lang racket

(define (my-div a b)
  ;; define inner recursive function, to get that sweet, sweet tail call
  (define (my-div-helper a b q)
    (cond
      [(< a b) q]
      [else
       (my-div-helper (- a b) b (+ 1 q))]))
  ;; call helper function, handling sign issues
  (cond
    [(and (< a 0) (> b 0)) (- 0 (my-div-helper (- 0 a) b 0))]
    [(and (> a 0) (< b 0)) (- 0 (my-div-helper a (- 0 b) 0))]
    [(and (< a 0) (< b 0)) (my-div-helper (- 0 a) (- 0 b) 0)]
    [else (my-div-helper a b 0)]))