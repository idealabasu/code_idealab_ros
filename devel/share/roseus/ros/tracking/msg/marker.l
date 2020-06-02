;; Auto-generated. Do not edit!


(when (boundp 'tracking::marker)
  (if (not (find-package "TRACKING"))
    (make-package "TRACKING"))
  (shadow 'marker (find-package "TRACKING")))
(unless (find-package "TRACKING::MARKER")
  (make-package "TRACKING::MARKER"))

(in-package "ROS")
;;//! \htmlinclude marker.msg.html


(defclass tracking::marker
  :super ros::object
  :slots (_color _x _y ))

(defmethod tracking::marker
  (:init
   (&key
    ((:color __color) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _color (string __color))
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:color
   (&optional __color)
   (if __color (setq _color __color)) _color)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; string _color
    4 (length _color)
    ;; float32 _x
    4
    ;; float32 _y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _color
       (write-long (length _color) s) (princ _color s)
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _color
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _color (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get tracking::marker :md5sum-) "9eab6da5b2968819e8b305355e8d814c")
(setf (get tracking::marker :datatype-) "tracking/marker")
(setf (get tracking::marker :definition-)
      "string color
float32 x
float32 y

")



(provide :tracking/marker "9eab6da5b2968819e8b305355e8d814c")


