;; Auto-generated. Do not edit!


(when (boundp 'universal_robots::position)
  (if (not (find-package "UNIVERSAL_ROBOTS"))
    (make-package "UNIVERSAL_ROBOTS"))
  (shadow 'position (find-package "UNIVERSAL_ROBOTS")))
(unless (find-package "UNIVERSAL_ROBOTS::POSITION")
  (make-package "UNIVERSAL_ROBOTS::POSITION"))

(in-package "ROS")
;;//! \htmlinclude position.msg.html


(defclass universal_robots::position
  :super ros::object
  :slots (_q _p ))

(defmethod universal_robots::position
  (:init
   (&key
    ((:q __q) (make-array 4 :initial-element 0.0 :element-type :float))
    ((:p __p) (make-array 3 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _q __q)
   (setq _p __p)
   self)
  (:q
   (&optional __q)
   (if __q (setq _q __q)) _q)
  (:p
   (&optional __p)
   (if __p (setq _p __p)) _p)
  (:serialization-length
   ()
   (+
    ;; float64[4] _q
    (* 8    4)
    ;; float64[3] _p
    (* 8    3)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[4] _q
     (dotimes (i 4)
       (sys::poke (elt _q i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[3] _p
     (dotimes (i 3)
       (sys::poke (elt _p i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[4] _q
   (dotimes (i (length _q))
     (setf (elt _q i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64[3] _p
   (dotimes (i (length _p))
     (setf (elt _p i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get universal_robots::position :md5sum-) "21488d769179605c39d61887a714ba19")
(setf (get universal_robots::position :datatype-) "universal_robots/position")
(setf (get universal_robots::position :definition-)
      "float64[4] q
float64[3] p

")



(provide :universal_robots/position "21488d769179605c39d61887a714ba19")


