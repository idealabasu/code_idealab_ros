
(cl:in-package :asdf)

(defsystem "force_plate-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "forces" :depends-on ("_package_forces"))
    (:file "_package_forces" :depends-on ("_package"))
  ))