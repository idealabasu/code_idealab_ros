
(cl:in-package :asdf)

(defsystem "ati_nano-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "write" :depends-on ("_package_write"))
    (:file "_package_write" :depends-on ("_package"))
  ))