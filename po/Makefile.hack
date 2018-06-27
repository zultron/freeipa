# Auxiliary target for translation maintainer:
# Strip untranslated strings and comments with code lines from the po files
# to make them smaller before storage in SCM.

DISTFILES.common.extra3 = Makefile.hack.in

IPA_TEST_I18N = ../ipatests/i18n.py
MSGATTRIB = /usr/bin/msgattrib

.PHONY: strip-po
strip-po:
	for po_file in $(POFILES); do \
		$(MSGATTRIB) --translated --no-fuzzy --no-location $$po_file > $$po_file.tmp || exit 1; \
		mv $$po_file.tmp $$po_file || exit 1; \
	done
	export FILES_TO_REMOVE=`find $(srcdir) -name '*.po' -empty` || exit 1; \
	if [ "$$FILES_TO_REMOVE" != "" ]; then \
		rm -v $$FILES_TO_REMOVE || exit 1; \
		echo; echo Please remove the deleted files from LINGUAS!; echo; \
	fi

clean: mostlyclean
	rm -f *~

# linters
test-gettext: $(DOMAIN).pot
	$(IPA_TEST_I18N) --test-gettext

validate-pot: $(DOMAIN).pot
	$(IPA_TEST_I18N) --show-strings --validate-pot $(DOMAIN).pot

validate-po: $(DOMAIN).pot
	$(IPA_TEST_I18N) --show-strings --validate-po $(POFILES)

# forcefully re-generate .pot file and test it
validate-src-strings: $(DOMAIN).pot-update
	$(MAKE) validate-pot
