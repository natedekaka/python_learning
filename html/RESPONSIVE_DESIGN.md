# Responsive Design Documentation
## SMAN Negeri 6 Cimahi - Python Learning Repository

---

## 📱 Responsive Breakpoints

Repository ini menggunakan **mobile-first approach** dengan breakpoints berikut:

### Breakpoints:
| Device | Width | Description |
|--------|-------|-------------|
| **Extra Small** | < 360px | Ponsel sangat kecil (iPhone SE, Samsung Galaxy J1) |
| **Small** | 360px - 480px | Ponsel standar (iPhone 6-8, Samsung Galaxy A10) |
| **Medium** | 480px - 768px | Ponsel besar & tablet kecil (iPad Mini) |
| **Large** | 768px - 1200px | Tablet & laptop kecil |
| **Extra Large** | ≥ 1200px | Desktop & laptop besar |

---

## 🎨 Responsive Features

### 1. **Navigation Bar**
- **Desktop (≥768px):** Menu horizontal penuh dengan spacing 2rem
- **Tablet (768px):** Menu lebih kompak, font 0.85rem
- **Mobile (<480px):** Navigasi stacked/vertikal, font 0.65rem
- **Extra Small (<360px):** Font sangat kecil 0.6rem, centered

### 2. **Hero Section**
- **Desktop:** H1 3.5rem, padding 5rem
- **Tablet:** H1 1.8rem, padding 3rem
- **Mobile:** H1 1.25rem, padding 1.5rem
- **Extra Small:** H1 1rem, padding minimal

### 3. **Cards Grid**
- **Desktop:** 3 kolom, gap 2.5rem
- **Tablet:** 2 kolom, gap 1.25rem
- **Mobile:** 1 kolom, gap 0.75rem

### 4. **Buttons**
- **Desktop:** Width auto, padding normal
- **Mobile:** Width 100% (full width), padding compact
- **Extra Small:** Padding minimal, font 0.65rem

### 5. **Code Blocks**
- **Desktop:** Font 1rem, full width
- **Tablet:** Font 0.7rem, overflow-x auto
- **Mobile:** Font 0.6rem, overflow-x auto
- **Extra Small:** Font 0.55rem, compacted

---

## 🔧 CSS Implementation

### Media Queries Digunakan:

```css
/* Tablet & below */
@media (max-width: 768px) { ... }

/* Mobile phones */
@media (max-width: 480px) { ... }

/* Extra small devices */
@media (max-width: 360px) { ... }

/* Large desktop */
@media (min-width: 1200px) { ... }
```

### Flexbox & Grid Responsiveness:

#### Navigation:
```css
/* Desktop */
.nav-links {
    display: flex;
    gap: 2rem;
}

/* Tablet */
@media (max-width: 768px) {
    .nav-links {
        gap: 0.5rem;
        flex-wrap: wrap;
    }
}
```

#### Cards:
```css
/* Desktop - 3 columns */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

/* Tablet - 2 columns */
@media (max-width: 768px) {
    .cards-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Mobile - 1 column */
@media (max-width: 480px) {
    .cards-grid {
        grid-template-columns: 1fr;
    }
}
```

---

## 📐 Layout Adjustments

### Container Padding:
| Breakpoint | Padding |
|-----------|---------|
| Desktop | 20px |
| Tablet | 15px |
| Mobile | 10px |
| Extra Small | 10px |

### Font Scaling:
- **Desktop:** 1rem base size
- **Tablet:** 0.95rem - 0.9rem
- **Mobile:** 0.85rem - 0.8rem
- **Extra Small:** 0.75rem - 0.7rem

### Spacing Adjustments:
```css
/* Desktop */
gap: 2rem;
padding: 2rem;
margin: 2rem 0;

/* Tablet */
gap: 1.25rem;
padding: 1.25rem;
margin: 1.25rem 0;

/* Mobile */
gap: 0.75rem;
padding: 0.75rem;
margin: 0.75rem 0;

/* Extra Small */
gap: 0.5rem;
padding: 0.5rem;
margin: 0.5rem 0;
```

---

## ✅ Testing Responsive

### Tested Devices:

**Phones:**
- ✅ iPhone SE (375px)
- ✅ iPhone 6-8 (375px)
- ✅ iPhone X/11 (375px)
- ✅ Samsung Galaxy S10 (360px)
- ✅ Samsung Galaxy A10 (720px)

**Tablets:**
- ✅ iPad Mini (768px)
- ✅ iPad Air (820px)
- ✅ iPad Pro (1024px)

**Desktops:**
- ✅ Laptop 13" (1280px)
- ✅ Monitor 15" (1366px)
- ✅ Monitor 24" (1920px)

### Browser DevTools:
Gunakan Chrome DevTools responsive mode untuk testing:
1. Buka DevTools (F12)
2. Click "Toggle device toolbar" (Ctrl+Shift+M)
3. Pilih berbagai devices atau custom width

---

## 🎯 Best Practices Diterapkan

1. **Mobile-First Approach:** Base styles untuk mobile, enhance untuk desktop
2. **Flexible Layouts:** Menggunakan Flexbox & CSS Grid
3. **Relative Units:** Em/Rem untuk font, percentage untuk width
4. **Touch-Friendly:** Buttons & links cukup besar untuk mobile
5. **Performance:** Minimal media queries, optimized CSS

---

## 📋 Responsive Elements Checklist

- ✅ Navigation responsive
- ✅ Hero section fluid
- ✅ Cards grid responsive
- ✅ Buttons full-width on mobile
- ✅ Code blocks scrollable
- ✅ Images responsive
- ✅ Tables scrollable
- ✅ Footer responsive
- ✅ Typography scales properly
- ✅ Spacing adjusts per breakpoint

---

## 🚀 Optimizations

1. **Viewport Meta Tag:** Sudah ada di semua HTML files
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```

2. **Flexible Images:** CSS ensures images scale responsively
   ```css
   img {
       max-width: 100%;
       height: auto;
   }
   ```

3. **CSS Grid & Flexbox:** Modern layout techniques
4. **Touch-Friendly:** Buttons & links dengan padding adequate
5. **Font Scaling:** Dynamic font sizes per breakpoint

---

## 📱 Viewing Recommendations

### Optimal Viewing:
- **Mobile:** Portrait mode, all orientations supported
- **Tablet:** Both portrait & landscape
- **Desktop:** Full width experience

### Browser Support:
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)

---

**Created by:** natedekaka  
**Sekolah:** SMAN Negeri 6 Cimahi  
**Updated:** 2026-04-10
