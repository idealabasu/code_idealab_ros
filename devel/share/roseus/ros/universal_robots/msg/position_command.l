;; Auto-generated. Do not edit!


(when (boundp 'universal_robots::position_command)
  (if (not (find-package "UNIVERSAL_ROBOTS"))
    (make-package "UNIVERSAL_ROBOTS"))
  (shadow 'position_command (find-package "UNIVERSAL_ROBOTS")))
(unless (find-package "UNIVERSAL_ROBOTS::POSITION_COMMAND")
  (make-package "UNIVERSAL_ROBOTS::POSITION_COMMAND"))

(in-package "ROS")
;;//! \htmlinclude position_command.msg.html


(defclass universal_robots::position_command
  :super ros::object
  :slots (_p ))

(defmethod universal_robots::position_command
  (:init
   (&key
    ((:p __p) (make-array 3 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _p __p)
   self)
  (:p
   (&optional __p)
   (if __p (setq _p __p)) _p)
  (:serialization-length
   ()
   (+
    ;; float64[3] _p
    (* 8    3)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[3] _p
     (dotimes (i 3)
       (sys::poke (elt _p i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[3] _p
   (dotimes (i (length _p))
     (setf (elt _p i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get universal_robots::position_command :md5sum-) "1abbaca176899a0863a2922ff57df9ac")
(setf (get universal_robots::position_command :datatype-) "universal_robots/position_command")
(setf (get universal_robots::position_command :definition-)
      "float64[3] p

")



(provide :universal_robots/position_command "1abbaca176899a0863a2922ff57df9ac")


